import javax.bluetooth.BluetoothStateException;
import javax.bluetooth.DeviceClass;
import javax.bluetooth.DiscoveryAgent;
import javax.bluetooth.DiscoveryListener;
import javax.bluetooth.LocalDevice;
import javax.bluetooth.RemoteDevice;
import javax.bluetooth.ServiceRecord;
import java.util.List;
import java.util.Arrays;
import java.util.Vector;
import java.util.Iterator;
import java.io.IOException;


class BtScanner{
    private Controlwindow cw;
    private String[] currentusers;
    private LocalDevice localdevice;
    private DiscoveryAgent discoveryagent;
    private boolean inquiring; 

    public BtScanner(Controlwindow a){
        this.cw = a;
        localdevice = LocalDevice.getLocalDevice();
        discoveryagent = localdevice.getDiscoveryAgent();
    }

    private synchronized String[] getnewusers(){
        BluetoothInquirer bi = new BluetoothInquirer();
        while(this.inquiring){
        }
        RemoteDevice[] temp = bi.getdevices();
        String[] ret = new String[temp.length];
        for(int i = 0, i < temp.length; i++){
            ret[i] = temp[i].getBluetoothAddress();
        }
        return ret;
    }

    public synchronized void updateusers(){
        String[] newuser;
        String[] lastusers;
        String[] tempusers;

        List<String> temp = Arrays.asList(this.getnewusers());
        tempusers = new String[temp.length];
        newuser = new String[temp.length];
        int j = 0;
        int k = 0;
        for(String i:this.currentusers){
            if(temp.contains(i)){
                tempusers[j] = i;
                j++;
                this.currentusers[j+k] = null;
            }else{
                newuser[k] = i;
                k++;
            }
        }

        String[] new2 = new String[k];
        System.arraycopy(newuser, 0, new2, 0, k-1);
        cw.newusers(new2);

        k = 0;
        String[] newlev = new String[this.currentusers.length-j];
        for(int t =  0; t < this.currentusers.length; t++){
            if(this.currentusers != null){
                newlev[k] = this.currentusers[t];
            }
        }
        cw.newlevers(newlev);
        
        tempusers = this.currentusers;
    }

    public abstract class BluetoothInquirer implements DiscoveryListener{
        boolean inquiring;
        DiscoveryAgent di;

        List devices;

        public boolean startInquiry() {
			inquiring = false;
			devices = new Vector();
            this.di = LocalDevice.getLocalDevice().getDiscoveryAgent();
			try {
				inquiring = di.startInquiry(DiscoveryAgent.GIAC, this);
			} catch (BluetoothStateException e) {
				System.err.println("Cannot start inquiry: " + e);
				return false;
			}
			return inquiring;
		}

        public RemoteDevice[] getdevices(){
            RemoteDevice returndevices =  di.retrieveDevices(DiscoveryAgent.CACHED);
        }
    }
}