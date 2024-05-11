package hash;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class LeituraArquivo {

    public static void main(String[] args) {
        System.out.println("xaaama");
        if (args.length < 1) {
            System.out.println("Uso: java LeituraArquivo <caminho_do_arquivo>");
            return;
        }

        String arquivoCaminho = args[0];

        try (BufferedReader br = new BufferedReader(new FileReader(new File(arquivoCaminho)))) {
            String linha;

            while ((linha = br.readLine()) != null) {
                System.out.println(linha); // Imprime cada linha lida do arquivo
            }
        } catch (IOException e) {
            System.err.println("Erro ao ler o arquivo: " + e.getMessage());
        }
    }
}
