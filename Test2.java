import java.util.Scanner;
 
public class Test2 {
 
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//1.键盘录入一个数字
		Scanner sc=new Scanner(System.in);
		String str;
		
		while(true) {
			
			System.out.println("请输入一个字符串：");
			str=sc.next();
			boolean flag=checkStr(str);
			if(flag) {
				break;
			}else {
				System.out.println("当前字符串不符合要求，请重新输入");
			}
		}
		
		for(int i=0;i<str.length();i++) {
			char c=str.charAt(i);
			String s=changeLuoMa(c);
			System.out.print(s+" ");
		}
		
 
	}
	public static String changeLuoMa(char number) {
		
		String str;
		switch(number) {
		case '0':str="";break;
		case '1':str="Ⅰ";break;
		case '2':str="Ⅱ";break;
		case '3':str="Ⅲ";break;
		case '4':str="Ⅳ";break;
		case '5':str="Ⅴ";break;
		case '6':str="Ⅵ";break;
		case '7':str="Ⅶ";break;
		case '8':str="Ⅷ";break;
		case '9':str="Ⅸ";break;
		default:str="";break;
		}
		return str;
		
	}
	//定义方法判断字符串是否符合要求
	public static boolean checkStr(String str) {
		//判断字符串长度是否小于等于9
		if(str.length()>9) {
			return false;
		}
		
		//判断字符串是否都是数字
		for(int i=0;i<str.length();i++) {
			char c=str.charAt(i);
			if(c<'0' || c>'9') {
				return false;
			}
		}
		
		return true;
	}
 
}