import 'package:flutter/material.dart';
import 'package:flutter_explained/utils/time_helper.dart';

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context){
    return Scaffold(
      body: Container(
        width: double.infinity,
        height: double.infinity,
        decoration: BoxDecoration(
          image: DecorationImage(
            image: AssetImage('assets/images/${TimeHelper.getTimeOfTheDay(DateTime.now())}.jpg'),
            fit: BoxFit.cover,
          ),
        ),
        child: Column(
          children: <Widget>[
            SizedBox(height: 64),
            FittedBox(
              child: Text(
                'Good ${TimeHelper.getTimeOfTheDay(DateTime.now())}',
                style: TextStyle(
                  fontSize: 48,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
          ]
        ),
      ),
    );
  }
}
