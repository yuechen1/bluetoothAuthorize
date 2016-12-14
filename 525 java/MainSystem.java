import support.User;

public class MainSystem{
    private Backserver backserver;
    private BtScanner  btscanner;
    private Controlwindow control;

    public MainSystem(){
        this.backserver = new Backserver();
        this.control = new Controlwindow(this.backserver);
        this.btscanner = new BtScanner(this.control);
        this.btscanner.start();
    }

    public void startshit(){
        String[] temp = {"Name1", "Name2"};
        Rule thisrule = new Rule(1, 2, temp, backserver.getuser(btscanner.getcurrent()));
        this.control.addrule(thisrule);
    }

    public void main(){
        MainSystem mymain = new MainSystem();
        mymain.startshit();
        while(true){
        }
    }

}