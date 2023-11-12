import 'package:flutter/material.dart';
import 'package:geo_quest/main.dart';

class WelcomePage extends StatefulWidget {
  @override
  _WelcomePageState createState() => _WelcomePageState();
}

class _WelcomePageState extends State<WelcomePage> {
  @override
  void initState() {
    super.initState();
    
    Future.delayed(const Duration(seconds: 5), () {
      Navigator.of(context).pushReplacement(MaterialPageRoute(
        builder: (context) => const MyHomePage(title: 'GeoQuest'),
      ));
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.blueGrey.shade900,
        elevation: 5,
        toolbarHeight: 24,
      ),
      body: Container(
        color: Colors.black,
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Image.asset("assets/giphy.gif", height: 200, width: 200),
              const Text(
                'Geo Quest',
                style: TextStyle(
                  fontSize: 70,
                  color: Colors.amber,
                  fontFamily: 'BleedingCowboys',
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}


