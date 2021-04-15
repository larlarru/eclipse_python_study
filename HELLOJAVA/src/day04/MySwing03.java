package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import com.sun.java.swing.plaf.windows.resources.windows;

import javax.swing.JTextArea;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.JComboBox;
import javax.swing.JTextField;

public class MySwing03 extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing03 frame = new MySwing03();
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
	public MySwing03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JTextArea ta = new JTextArea();
		ta.setBounds(32, 10, 362, 24);
		contentPane.add(ta);
		
		JButton btn1 = new JButton("1");
		btn1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				//String str_old = ta.getText();
				String str_old = ta.getText();
				String str_new = ((JButton)e.getSource()).getText();
				//ta.setText(str_old + 1);
				ta.setText(str_old + str_new);
			}
		});
		btn1.setBounds(32, 44, 49, 36);
		contentPane.add(btn1);
		
		JButton btn2 = new JButton("2");
		btn2.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String str_old = ta.getText();
				ta.setText(str_old + 2);
			}
		});
		btn2.setBounds(103, 44, 49, 36);
		contentPane.add(btn2);
		
		JButton btn3 = new JButton("3");
		btn3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String str_old = ta.getText();
				ta.setText(str_old + 3);
			}
		});
		btn3.setBounds(176, 44, 49, 36);
		contentPane.add(btn3);
		
		JButton btn6 = new JButton("6");
		btn6.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String str_old = ta.getText();
				ta.setText(str_old + 6);
			}
		});
		btn6.setBounds(176, 90, 49, 36);
		contentPane.add(btn6);
		
		JButton btn5 = new JButton("5");
		btn5.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String str_old = ta.getText();
				ta.setText(str_old + 5);
			}
		});
		btn5.setBounds(103, 90, 49, 36);
		contentPane.add(btn5);
		
		JButton btn4 = new JButton("4");
		btn4.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String str_old = ta.getText();
				ta.setText(str_old + 4);
			}
		});
		btn4.setBounds(32, 90, 49, 36);
		contentPane.add(btn4);
		
		JButton btn9 = new JButton("9");
		btn9.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String str_old = ta.getText();
				ta.setText(str_old + 9);
			}
		});
		btn9.setBounds(176, 137, 49, 36);
		contentPane.add(btn9);
		
		JButton btn8 = new JButton("8");
		btn8.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String str_old = ta.getText();
				ta.setText(str_old + 8);
			}
		});
		btn8.setBounds(103, 137, 49, 36);
		contentPane.add(btn8);
		
		JButton btn7 = new JButton("7");
		btn7.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String str_old = ta.getText();
				ta.setText(str_old + 7);
			}
		});
		btn7.setBounds(32, 137, 49, 36);
		contentPane.add(btn7);
		
		JButton btn0 = new JButton("0");
		btn0.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String str_old = ta.getText();
				ta.setText(str_old + 0);
			}
		});
		btn0.setBounds(32, 181, 49, 36);
		contentPane.add(btn0);
		
		JButton btnclick = new JButton("call");
		btnclick.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				JOptionPane.showMessageDialog(null, ta.getText() + " 전화중 입니다.");
			}
		});
		btnclick.setBounds(113, 188, 97, 23);
		contentPane.add(btnclick);
	}
}


