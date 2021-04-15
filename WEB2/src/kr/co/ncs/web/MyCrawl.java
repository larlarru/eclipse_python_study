package kr.co.ncs.web;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

//@WebServlet("/mycrawl")
public class MyCrawl extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setCharacterEncoding("UTF-8");
		try {
			HttpSession session = request.getSession();
			String username  = session.getAttribute("user_name").toString();
			response.getWriter().append("<table><tr><td>Hwang si yon</td></tr></table>");
		} catch (Exception e) {
			response.getWriter().append("you have no authority for this page");
		}
//		response.getWriter().append("<table><tr><td>황시연</td></tr></table>");
		
	}
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
