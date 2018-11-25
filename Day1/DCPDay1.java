import java.* ; 
/**
 * 
 */
public class DCPDay1 {
    /**  */
    public static final int K = 17 ; 
    /**  */
    HashMap map = new HashMap<int,boolean>();

    public static void main(String[] args){
        if (args.lenth < 2 || (args == null){
            print("Invalid input") ; 
        }else{
            int tmp;
            for(String value: args){
                tmp = String.parseInt(value);
                if(map.getValue(tmp)){
                    print("Sucessful response") ; 
                    return true ; 
                }else{
                    map.putKey(K-tmp,true) ; 
                }
            }
        }
    }
}