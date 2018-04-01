public class HelloWorld2 {

    public static void main(String[] args) {
        System.out.println("Hello World :)");
        System.out.println("This time the flag not \"given\" to you already");
        System.out.println("You have to dig deeper yourself =D");

        String charset[]={"", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_", "{", "}"};
		String flag=charset[7]+charset[3]+charset[20]+charset[6]+charset[38]+charset[20]+charset[8]+charset[28]+charset[19]+charset[37]+charset[27]+charset[14]+charset[30]+charset[37]+charset[22]+charset[30]+charset[18]+charset[25]+charset[37]+charset[8]+charset[31]+charset[18]+charset[4]+charset[37]+charset[20]+charset[27]+charset[37]+charset[6]+charset[28]+charset[12]+charset[12]+charset[39];
		//GCTF{th1s_0n3_v3ry_l0ng_t0_c0de}
		System.out.println(flag);
	}
}
