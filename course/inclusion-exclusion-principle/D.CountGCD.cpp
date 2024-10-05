#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

const long long MOD = 998244353;

// Função para obter os fatores primos de um número
vector<long long> prime_factors(long long n) {
    vector<long long> factors;
    if (n % 2 == 0) {
        factors.push_back(2);
        while (n % 2 == 0) {
            n /= 2;
        }
    }
    for (long long i = 3; i * i <= n; i += 2) {
        if (n % i == 0) {
            factors.push_back(i);
            while (n % i == 0) {
                n /= i;
            }
        }
    }
    if (n != 1) {
        factors.push_back(n);
    }
    return factors;
}

// Função para calcular os múltiplos corretos
long long correctMultiples(long long m, long long prev, long long current) {
    vector<long long> uselessNumbers = prime_factors(prev / current);
    long long totalMultiples = m / current;
    long long res = totalMultiples % MOD;
    int sz = uselessNumbers.size();

    for (int i = 1; i < (1 << sz); ++i) {
        long long cr = 1;
        int bits = 0;
        for (int j = 0; j < sz; ++j) {
            if ((i >> j) & 1) {
                cr *= uselessNumbers[j];
                bits += 1;
            }
        }
        long long delta = (totalMultiples / cr) % MOD;
        if (bits % 2 == 0) {
            res = (res + delta) % MOD;
        } else {
            res = (res - delta + MOD) % MOD;
        }
    }
    return res;
}

// Função para resolver cada caso de teste
long long solve() {
    int n;
    long long m;
    cin >> n >> m;
    vector<long long> lista(n);
    for (int i = 0; i < n; ++i) {
        cin >> lista[i];
    }

    for (int i = 0; i < n - 2; ++i) {
        if (lista[i] % lista[i + 1] != 0) {
            return 0;
        }
    }

    long long res = 1;
    for (int i = 1; i < n; ++i) {
        if (lista[i] == lista[i - 1]) {
            res = res * (m / lista[i]) % MOD;
        } else {
            res = res * correctMultiples(m, lista[i - 1], lista[i]) % MOD;
        }
    }
    return res;
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cout << solve() << endl;
    }
    return 0;
}
