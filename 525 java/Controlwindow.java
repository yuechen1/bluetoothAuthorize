import java.util.Iterator;
import java.util.Vector;
import support.User;

class Controlwindow{
    Backserver serv;
    Vector<Rule> rules;

    public Controlwindow(Backserver b){
        this.rules = new Vector(3,1);
        this.serv = b;
    }

    public void addrule(Rule u){
        rules.add(u);
        u.start();
    }

    public void newusers(String[] bid){
        Rule temp;
        Iterator<Rule> temprule = this.rules.iterator();
        User[] users = serv.getuser(bid);
        while(temprule.hasNext()){
            temp = temprule.next();
            temp.updateuseradd(users);
        }
    }

    public void newleavers(String[] bid){
        Rule temp;
        Iterator<Rule> temprule = this.rules.iterator();
        User[] users = serv.getuser(bid);
        while(temprule.hasNext()){
            temp = temprule.next();
            temp.updateuserdel(users);
        }
    }

}