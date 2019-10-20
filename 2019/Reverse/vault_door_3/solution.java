public class name{
public static void main(String[] args){

String p = "jU5t_a_sna_3lpm16g84c_u_4_m0r846";

char[] buffer = new char[32];
int i;
for (i=0; i<8; i++) {
    buffer[i] = p.charAt(i);
}
for (; i<16; i++) {
    buffer[i] = p.charAt(23-i);
}
for (; i<32; i+=2) {
    buffer[i] = p.charAt(46-i);
}
for (i=31; i>=17; i-=2) {
    buffer[i] = p.charAt(i);
}
String s = new String(buffer);
System.out.println(s);

}
}