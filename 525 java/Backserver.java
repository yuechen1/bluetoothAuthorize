import java.util.Vector;
import support.User;
import java.util.Arrays;

class Backserver{
    Thread t;
    private Vector<User> users;

    public Backserver(){
        String tempstring;
        users = new Vector(4,1);
        for(int i = 0; i < 4; i++){
            tempstring = String.valueOf(i);
            User tempuser = new User("Name" + tempstring, 1, tempstring, "here", "none");
            this.users.addElement(tempuser);
        }
    }

    public boolean deleteuser(User n){
        return this.users.remove(n);
    }

    public User[] getuser(String[] n){
        User[] returnuser;
        User[] notuser = new User[n.length];
        int userfound = 0;
        User[] tempusers = new User[users.size()];
        users.toArray(tempusers);
        for(String nname:n){
            for(int i = 0;i < tempusers.length; i++)
            {
                if(n.equals(tempusers[i].getblueid()))
                {
                    notuser[userfound] = tempusers[i];
                    userfound++;
                }
            }
        }
        returnuser = new user[userfound];
        System.arraycopy(notuser, 0, returnuser, 0, userfound);
        return returnuser;
    }
}