import java.applet.*;
import java.awt.*;
import java.awt.event.*;


<Applet code="Pro9" width="400" height="400"></Applet> 
public class mouseBG extends Applet implements MouseListener{
    public void init() {
            addMouseListener(this);
            
    }
    public void mouseEntered(MouseEvent e) {
        setBackground(Color.blue);
    }
    public void mouseExited(MouseEvent e) {
        setBackground(Color.red);
    }
    public void mouseClicked(MouseEvent e) {
        setBackground(Color.green);        
    }
    public void mousePressed(MouseEvent e) {
        setBackground(Color.cyan);
    }
    public void mouseReleased(MouseEvent e) {
        setBackground(Color.magenta);
    }
}
