package Lectures;

// Создание файла, запись\дозапись в него

// import java.io.FileWriter;
// import java.io.IOException;
// public class Lec10Files {
//     public static void main(String[] args) {
//         try (FileWriter fw = new FileWriter("file.txt", false)) {   //false - создать файл, true - дописать в файл
//             fw.write("line 1");
//             fw.append('\n');
//             fw.append('2');
//             fw.append('\n');
//             fw.write("line 3");
//             fw.flush();
//         } catch (IOException ex) {
//             System.out.println(ex.getMessage());   // Обработка ошибок 
//         }
//     } }

// Чтение из файла (посимвольно)
// import java.io.*;

// public class Lec10Files {
//     public static void main(String[] args) throws Exception {
//         FileReader fr = new FileReader("file.txt");
//         int c;
//         while ((c = fr.read()) != -1) {
//             char ch = (char) c;
//             if (ch == '\n') {
//                 System.out.print(ch);
//             } else {
//                 System.out.print(ch);
//             }
//         }

//     }}

// Чтение из файла (построчно)
// import java.io.*;

// public class Program {
//     public static void main(String[] args) throws Exception {
//         BufferedReader br = new BufferedReader(new FileReader("file.txt"));
//         String str;
//         while ((str = br.readLine()) != null) {
//             System.out.printf("== %s ==\n", str);
//         }
//         br.close();
//     }
// }
