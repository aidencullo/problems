package LLMerge;

import java.io.File;
import java.util.Scanner;
import java.util.ArrayList;

public class ReadFile
{
  public static ArrayList<String> read(String fileName) throws Exception
  {
    // pass the path to the file as a parameter
    File file = new File(fileName);
    Scanner sc = new Scanner(file);
    ArrayList<String> inputLines = new ArrayList<String>();
    
    while (sc.hasNextLine()){
	inputLines.add(sc.nextLine());
    }
    return inputLines;
  }
}
