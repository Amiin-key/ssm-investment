import 'package:flutter/material.dart';
import 'dart:async';

void main() => runApp(SSMApp());

class SSMApp extends StatefulWidget {
  @override
  _SSMAppState createState() => _SSMAppState();
}

class _SSMAppState extends State<SSMApp> {
  bool isSomali = true; // Luuqadda toggle

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData.dark().copyWith(
        scaffoldBackgroundColor: Color(0xFF111111),
        primaryColor: Color(0xFF00FF7F),
      ),
      home: LoginScreen(isSomali: isSomali, toggleLang: () => setState(() => isSomali = !isSomali)),
    );
  }
}

// --- 1. LOGIN SCREEN ---
class LoginScreen extends StatelessWidget {
  final bool isSomali;
  final VoidCallback toggleLang;
  LoginScreen({required this.isSomali, required this.toggleLang});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: EdgeInsets.all(25.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text("SSM PRO", style: TextStyle(fontSize: 40, fontWeight: FontWeight.bold, color: Color(0xFF00FF7F))),
            SizedBox(height: 10),
            Text(isSomali ? "Ku soo dhawoow Maal-gashiga" : "Welcome to Investing", style: TextStyle(color: Colors.grey)),
            SizedBox(height: 50),
            TextField(decoration: InputDecoration(labelText: isSomali ? "Username" : "Username", border: OutlineInputBorder())),
            SizedBox(height: 15),
            TextField(obscureText: true, decoration: InputDecoration(labelText: isSomali ? "Password" : "Password", border: OutlineInputBorder())),
            SizedBox(height: 30),
            ElevatedButton(
              style: ElevatedButton.styleFrom(backgroundColor: Color(0xFF00FF7F), minimumSize: Size(double.infinity, 50)),
              onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (context) => Dashboard(isSomali: isSomali))),
              child: Text(isSomali ? "GAL APP-KA" : "LOGIN", style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold)),
            ),
            TextButton(onPressed: toggleLang, child: Text(isSomali ? "Switch to English" : "U beddel Soomaali")),
          ],
        ),
      ),
    );
  }
}

// --- 2. DASHBOARD ---
class Dashboard extends StatefulWidget {
  final bool isSomali;
  Dashboard({required this.isSomali});

  @override
  _DashboardState createState() => _DashboardState();
}

class _DashboardState extends State<Dashboard> {
  double balance = 1500.50;
  double btcPrice = 67450.0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("SSM PORTFOLIO"),
        backgroundColor: Color(0xFF1A1C1E),
        actions: [IconButton(icon: Icon(Icons.notifications), onPressed: () {})],
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: EdgeInsets.all(20.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Balance Card
              Container(
                width: double.infinity,
                padding: EdgeInsets.all(25),
                decoration: BoxDecoration(
                  color: Color(0xFF102A12),
                  borderRadius: BorderRadius.circular(20),
                  border: Border.all(color: Color(0xFF00FF7F), width: 1),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(widget.isSomali ? "HANTIDA GUUD" : "TOTAL WEALTH", style: TextStyle(color: Color(0xFF00FF7F), fontSize: 12)),
                    SizedBox(height: 10),
                    Text("\$${balance.toStringAsFixed(2)}", style: TextStyle(fontSize: 35, fontWeight: FontWeight.bold)),
                  ],
                ),
              ),
              SizedBox(height: 30),
              Text(widget.isSomali ? "Suuqa Live-ka ah" : "Live Markets", style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
              SizedBox(height: 15),
              // Crypto Price Card
              ListTile(
                backgroundColor: Color(0xFF1A1C1E),
                leading: CircleAvatar(backgroundColor: Colors.orange, child: Text("B", style: TextStyle(color: Colors.white))),
                title: Text("Bitcoin (BTC)"),
                trailing: Text("\$${btcPrice.toStringAsFixed(2)}", style: TextStyle(color: Color(0xFF00FF7F), fontWeight: FontWeight.bold)),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
              ),
              SizedBox(height: 40),
              // EVC Plus Helper Button
              ElevatedButton.icon(
                style: ElevatedButton.styleFrom(backgroundColor: Colors.blue, minimumSize: Size(double.infinity, 55)),
                icon: Icon(Icons.phone_android, color: Colors.white),
                label: Text(widget.isSomali ? "KU SHUBO EVC PLUS" : "DEPOSIT VIA EVC PLUS"),
                onPressed: () => _showEVCHelper(context),
              ),
            ],
          ),
        ),
      ),
    );
  }

  // --- EVC PLUS HELPER DIALOG ---
  void _showEVCHelper(BuildContext context) {
    showModalBottomSheet(
      context: context,
      backgroundColor: Color(0xFF1A1C1E),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.vertical(top: Radius.circular(25))),
      builder: (context) {
        return Padding(
          padding: EdgeInsets.all(25),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Text(widget.isSomali ? "Habka Lacag Ku Shubista" : "How to Deposit", style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Color(0xFF00FF7F))),
              SizedBox(height: 20),
              Text(widget.isSomali ? "1. Garaac *712*" : "1. Dial *712*", style: TextStyle(fontSize: 16)),
              Text(widget.isSomali ? "2. U dir lacagta: 061XXXXXXX" : "2. Send money to: 061XXXXXXX", style: TextStyle(fontSize: 16)),
              Text(widget.isSomali ? "3. Nuqul ka qaado TXID-ga" : "3. Copy the TXID", style: TextStyle(fontSize: 16)),
              SizedBox(height: 20),
              ElevatedButton(onPressed: () => Navigator.pop(context), child: Text("OK")),
            ],
          ),
        );
      },
    );
  }
}
