import support.User;

public class MainSystem{
    private Backserver backserver;
    private BtScanner  btscanner;
    private Controlwindow  control;

    public MainSystem(){
        this.backserver = new Backserver();
        this.btscanner = new BtScanner();
    }

}