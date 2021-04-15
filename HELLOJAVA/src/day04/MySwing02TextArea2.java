package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JTextArea;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing02TextArea2 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing02TextArea2 frame = new MySwing02TextArea2();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing02TextArea2() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JTextArea ta = new JTextArea();
		ta.setBounds(12, 8, 116, 253);
		contentPane.add(ta);
		
		tf = new JTextField();
		tf.setBounds(140, 10, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JLabel lb1 = new JLabel("New label");
		lb1.setBounds(268, 13, 57, 15);
		contentPane.add(lb1);
		
		JButton btn = new JButton("click");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				int num1 = Integer.parseInt(tf.getText());
				String res = num1 + " * " + 1 + " = " + Integer.toString(num1*1) + "\n";
				res += num1 + " * " + 2 + " = " + Integer.toString(num1*2) + "\n";
				res += num1 + " * " + 3 + " = " + Integer.toString(num1*3) + "\n";
				res += num1 + " * " + 4 + " = " + Integer.toString(num1*4) + "\n";
				res += num1 + " * " + 5 + " = " + Integer.toString(num1*5) + "\n";
				res += num1 + " * " + 6 + " = " + Integer.toString(num1*6) + "\n";
				res += num1 + " * " + 7 + " = " + Integer.toString(num1*7) + "\n";
				res += num1 + " * " + 8 + " = " + Integer.toString(num1*8) + "\n";
				res += num1 + " * " + 9 + " = " + Integer.toString(num1*9) + "\n";
				ta.setText(res);
				
				
				
			}
		});
		btn.setBounds(140, 41, 97, 23);
		contentPane.add(btn);
	}
}
