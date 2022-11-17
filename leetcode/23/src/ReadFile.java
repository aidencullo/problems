package LLMerge;

import java.io.File;
import java.util.Scanner;

public class ReadFile
{
  public static void read(String fileName) throws Exception
  {
    // pass the path to the file as a parameter
    File file = new File(fileName);
    Scanner sc = new Scanner(file);
 
    while (sc.hasNextLine())
      System.out.println(sc.nextLine());
  }
}
