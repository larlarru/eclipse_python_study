package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.JLabel;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class MySwing03 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;
	private JTextField tf4;
	private JTextField tf5;
	private JTextField tf6;
	private JButton btn1;
	private JButton btn2;

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
		
		tf1 = new JTextField();
		tf1.setBounds(0, 89, 78, 31);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		tf2 = new JTextField();
		tf2.setColumns(10);
		tf2.setBounds(170, 89, 71, 31);
		contentPane.add(tf2);
		
		JLabel lb1 = new JLabel("+");
		lb1.setBounds(133, 97, 29, 15);
		contentPane.add(lb1);
		
		tf3 = new JTextField();
		tf3.setColumns(10);
		tf3.setBounds(334, 89, 88, 31);
		contentPane.add(tf3);
		
		tf4 = new JTextField();
		tf4.setColumns(10);
		tf4.setBounds(12, 175, 78, 31);
		contentPane.add(tf4);
		
		tf5 = new JTextField();
		tf5.setColumns(10);
		tf5.setBounds(156, 171, 78, 31);
		contentPane.add(tf5);
		
		tf6 = new JTextField();
		tf6.setColumns(10);
		tf6.setBounds(326, 175, 78, 31);
		contentPane.add(tf6);
		
		JLabel lb3 = new JLabel("에서");
		lb3.setBounds(102, 183, 42, 15);
		contentPane.add(lb3);
		
		btn1 = new JButton("=");
		btn1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int num1 = Integer.parseInt(tf1.getText());
				int num2 = Integer.parseInt(tf2.getText());
				int sum = num1 + num2;
				tf3.setText(Integer.toString(sum));
				
			}
		});
		btn1.setBounds(253, 93, 69, 23);
		contentPane.add(btn1);
		
		btn2 = new JButton("합은");
		btn2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				int num3 = Integer.parseInt(tf4.getText());
				int num4 = Integer.parseInt(tf5.getText());
				if(num4 < num3) tf6.setText("두번째 칸의 수가 작습니다. 다시 입력하세요.");
				else {
					int sum = 0;
					for(int i=num3; i <= num4; i++) {
						sum += i;
					}
					tf6.setText(Integer.toString(sum));
				}
				
			}
		});
		btn2.setBounds(258, 179, 56, 23);
		contentPane.add(btn2);
	}
}
