package support;
/**
 * User
 * holds all relivent data for a user 
 */
public class User {
    private String name;    //name of user
    private int privilege;  //position of user
    private String blueid;  //bluetooth id associated with the user
    private String department; //department the user belong to
    private String attribute;

    public User (String a, int priv, String bid, String dep, String at) {
        this.name = a;
        this.privilege = priv;
        this.blueid = bid;
        this.department = dep;
        this.attribute = at;
    }

    public String getattribute(){
        return this.attribute;
    }

    public String getname(){
        return this.name;
    }

    public Int getprivilege(){
        return this.privilege;
    }

    public String getblueid(){
        return this.blueid;
    }

    public String getdepartment(){
        return this.department;
    }
}