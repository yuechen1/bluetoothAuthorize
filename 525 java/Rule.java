import java.lang.Thread;
import java.util.Vector;
import java.util.Arrays;
import java.util.List;
import java.util.Iterator;
/**
 * name
 */
class Rule implements Runnable{
    private Thread t;
    //TODO: needs an object
    private List<String> access;
    private int rulesetnumber;
    private int minnumber;
    private Vector<User> currentuser;
    /*
    * 1 = only users in access array is allowed, the name is used as the identifier here
    * 2 = only users with this attribute in this array is allowed
    * 3 = only users with above this position is allowed
    * 4 = only users with above first position and have all attribute is allowed
    */
    public Rule (int a, int b, String[] c, User[] u) {
        this.currentuser = new Vector(3,1);
        this.access = Array.asList(c);
        this.rulesetnumber = a;
        this.minnumber = b;
        if(b < 1 || a < 1 || a > 4){
            this.rulesetnumber = -1;
        }
        else{
            this.updateuseradd(u);
        }
    }
    
    public void start(){
        t = new Thread(this, "thisThread");
        t.start();
    }

    public void run(){
        while(true){
            while(checkrule()){
                System.out.println("this rule is working");
                //todo turn object on
                Thread.sleep(5000);
            }
            while(!checkrule()){
                //todo turn object off
                Thread.sleep(1000);
            }
        }
    }

    //Add users to current user
    public synchronized void updateuseradd(User[] u){
        boolean k;
        if(rulesetnumber = 1)
        {
            for(User i : u){
                if(access.contains(i.getname())){
                    k = currentuser.add(i)
                }
            }
        }
        return;
    }

    //remove users from current user
    public synchronized void updateuserdel(User[] u){
        boolean k;
        if(rulesetnumber = 1)
        {
            for(User i : u){
                if(access.contains(i.getname())){
                    k = currentuser.remove(i)
                }
            }
        }
        return;
    }
    
    //check the rule against the current users
    private synchronized boolean checkrule(){
        boolean hn;
        int tempcount = this.minnumber;
        Iterator<User> temparray = this.currentuser.iterator();
        User temp;
        if(rulesetnumber == 1)
        {
            while(temparray.hasNext()){
                temp = temparray.next();
                if(access.contains(temp.getname())){
                    tempcount--;
                    if(tempcount == 0){
                        return true;
                    }
                }
            }
            return false;
        }else if(rulesetnumber == 2){
            while(temparray.hasNext()){
                temp = temparray.next();
                if(access.contains(temp.getattribute())){
                    tempcount--;
                    if(tempcount == 0){
                        return true;
                    }
                }
            }
            return false;
        }else if(rulesetnumber == 3){
            Int p = Integer.parseInt(access.get(0));
            while(temparray.hasNext()){
                temp = temparray.next();
                if(p <= temp.getprivilege()){
                    tempcount--;
                    if(tempcount == 0){
                        return true;
                    }
                }
            }
            return false;
        }else{
            Int p = Integer.parseInt(access.get(0));
            while(temparray.hasNext()){
                temp = temparray.next();
                if(access.contains(temp.getattribute())){
                    tempcount--;
                    if(tempcount == 0){
                        return true;
                    }
                }
            }
            return false;
        }
    }
    
    public int getminnumber(){
        return this.minnumber;
    }

    public int getrulesetnumber(){
        return this.rulesetnumber;
    }
}