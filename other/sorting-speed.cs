using System;

// Measures and compares the runtime and space complexity of multiple sorting algorithms as input size scales
					
public class Program
{
	public int[] bubbleSort(int[] list)
	{
		while(true){
			bool swapped = false;
			
			for(int i=0; i < list.Length - 1; i++)
			{
				int a = list[i];
				int b = list[i + 1];

				if(a > b)
				{
					list[i] = b;
					list[i + 1] = a;
					swapped = true;
				}
			}
			if(!swapped){break;}
		}
		return list;
	}
	
	public void InsertionSort(int[] list)
	{
		// [5, 1, 3, 4, 6, 2, 8]
		
		for(int i=1; i<list.Length; i++)
		{
			
			int current = list[i];
			int left = i - 1;
			
			while(left >= 0 && list[left] > current)
			{
				list[left + 1] = list[left];
				left--;
				
			}
			
			
			
		}
	}
	
	
	
	
	
	
	public void Printer(int[] list)
	{
		foreach(int val in list)
		{
			Console.Write(val + " ");
		}
		Console.Write("\n\n");
	}
		
	
	
	public static void Main()
	{
		int[] list = {47, 2, 91, 34, 67, 15, 83, 29, 56, 72, 8, 44, 61, 37, 95, 13, 78, 52, 26, 69, 5, 88, 41, 63, 19};
		
		Program p = new Program();
		p.Printer(list);  
		p.bubbleSort(list);
		p.Printer(list);
	}
}




//47, 2, 91, 34, 67, 15, 83, 29, 56, 72, 8, 44, 61, 37, 95, 13, 78, 52, 26, 69, 5, 88, 41, 63, 19
//bubble sort
//selection sort
//insertion sort
//merge sort
//quick sort
//heap sort
//
