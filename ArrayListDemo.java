import java.util.ArrayList;

public class ArrayListExample {
    public static void main(String[] args) {
        // 创建ArrayList
        ArrayList<String> arrayList = new ArrayList<>();

        // 添加元素
        arrayList.add("Apple");
        arrayList.add("Banana");
        arrayList.add("Orange");

        // 获取元素
        String firstElement = arrayList.get(0);
        System.out.println("第一个元素是：" + firstElement); // Output: 第一个元素是：Apple

        // 修改元素
        arrayList.set(1, "Grapes");
        System.out.println("修改后的元素是：" + arrayList); // Output: 修改后的元素是：[Apple, Grapes, Orange]

        // 删除元素
        arrayList.remove(2);
        System.out.println("删除后的元素是：" + arrayList); // Output: 删除后的元素是：[Apple, Grapes]
    }
}