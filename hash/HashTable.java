package hash;

import java.util.LinkedList;

public class HashTable<K, V>{
    private Entry<K, V>[] table;

    public HashTable(int size){
        table = new Entry[size];
        for(int i = 0; i < size; i ++){
            table[i] = new Entry<K, V>(null, null);
        }

    }

    private static class Entry<K, V> {
        char status;
        K chave;
        LinkedList<V> valores;

        public Entry(K chave, V valor) {
            this.status = 'L';
            this.chave = chave;
            this.valores = new LinkedList<>();
        }
    }

    private int calcularIndice(K chave) {
        return Math.abs(chave.hashCode() % table.length);
    }

    private int getIndexKey(K chave){
        int indice = calcularIndice(chave);
        int start = indice;
        do{
            if(table[indice].chave.equals(chave)){
                return indice;
            }
            indice = (indice + 1) % table.length;
        }while(start != indice);
        return -1;
    }

    public void put(K chave, V valor){
        int indice = calcularIndice(chave);
        int start = indice;
        do{
            if(table[indice].status == 'L' || table[indice].status == 'R' || table[indice].chave.equals(chave)){
                table[indice].status = 'O';
                table[indice].chave = chave;
                table[indice].valores.add(valor);
                break;
            }
            indice = (indice + 1) % table.length;
        }while(indice != start);


    }


    public LinkedList<V> get(K chave){
        int indice = getIndexKey(chave);
        if(indice != -1){
            return table[indice].valores;
        }

        return null;
    }

    public void remove(K chave){
        int indice = getIndexKey(chave);

        if(indice != -1){
        
            table[indice].status = 'R';
            table[indice].chave = null;
            table[indice].valores.clear();
        }
        
    }

    public void imprimirHash(){
        for(int i = 0; i < table.length; i ++){
            System.out.println("Indice " + i + " | Chave: " + table[i].chave + " | Status: " + table[i].status);
            for (int j = 0; j < table[i].valores.size(); j++){
                System.out.print(table[i].valores.get(j) + " ");
            }
            System.out.println();

        }
    }

    public static void main(String[] args){
        HashTable<Integer, Integer> meuHash = new HashTable<>(10);
        meuHash.put(1, 1);
        meuHash.put(1, 2);
        meuHash.put(1, 3);
        meuHash.put(1, 4);
        meuHash.put(200, 1);
        meuHash.put(100, 2);
        meuHash.put(7, 2);
        meuHash.put(3, 2);
        meuHash.put(11, 2);
        meuHash.put(12, 2);
        meuHash.put(4, 2);
        meuHash.put(5, 2);
        meuHash.put(6, 2);
        meuHash.put(8, 2);

        meuHash.imprimirHash();
        System.out.println("\n\n\n");
        meuHash.remove(100);
        meuHash.put(8, 2);
        meuHash.imprimirHash();
        
    }




}