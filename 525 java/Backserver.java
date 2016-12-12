import java.util.Vector;
import supoort.User;

class Backserver{
    
    private Vector users;

    public Backserver(){
        String tempstring;
        users = new Vector(4,1);
        for(int i = 0; i < 4; i++){
            tempstring = String.valueOf(i);
            User tempuser = new User("Name" + tempstring, 1, tempstring, "here");
            this.users.addElement(tempuser);
        }
        return;
    }


    public void adduser(User u){
        this.users.addElement(u);
        return;
    }


    public boolean deleteuser(User n){
        return this.users.remove(n)
    }

    public User[] getuser(String[] n){
        User[] returnuser;
        User[] notuser = new User[n.length];
        Int userfound = 0
        User[] tempusers = this.users.toArray();
        for(String nname:n){
            for(int i = 0;i < tempusers.length(); i++)
            {
                if(n.equals(tempusers[i].blueid()))
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