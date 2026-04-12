using System;

//given a list of integers, sort the list recursively using tree sort.
					
public class Program
{
	//single tree node
	public class Node
	{
		public int data;     //data
		public Node? left;   //left child
		public Node? right;  //right child
		
		public Node(int data)
		{
			this.data = data;
			this.left = null;
			this.right = null;
		}
	}
	
	public class Tree
	{
		private Node? root;
		
		public Tree(){this.root = null;}
		
		public void addNode(int data)
		{
			Node new_node = new Node(data);
			
			//case tree empty
			if (this.root == null) 
			{
				root = new_node;
				return;
			}
			
			//traverse tree
			Node current = root;
			while(current != null)
			{
				if(new_node.data < current.data){
					if(current.left == null)
					{
						current.left = new_node;
						break;
					}
					current = current.left;
				}
				else
				{
					if(current.right == null)
					{
						current.right = new_node;
						break;
					}
					current = current.right;
				}
			}
		}
		
		//print tree nodes in-order (recursive traversal)
		private void treeDisplay(Node current) 
		{
			//base case, don't go deeper
			if(current == null){return;}
			treeDisplay(current.left);
			Console.Write(current.data + "->");
			treeDisplay(current.right);
		}
		
		public void treeDisplay()
		{
			Console.Write("In-order: ");
			treeDisplay(this.root);
			Console.Write("NULL\n");
		}
	}
	
	public static void Main()
	{
		int[] values = {5, 3, 7, 2, 4, 6, 8, 1};
		Tree tree = new Tree();
		
		Console.Write("Original: ");
		foreach(int val in values){
			Console.Write(val + "->");
			tree.addNode(val);
		}
		
		Console.Write("NULL\n\n");
		
		tree.treeDisplay();
	}
}
