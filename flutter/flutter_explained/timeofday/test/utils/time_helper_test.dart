import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_explained/utils/time_helper.dart';

void main () {

  group('TimeHelper', () {
    
    test('should return Night', () {
      DateTime time = DateTime(2021, 1, 1, 5);
      String timeOfDay = TimeHelper.getTimeOfTheDay(time);
      expect(timeOfDay, 'Night');
    });
    
    test('should return Morning', () {
      DateTime time = DateTime(2021, 1, 1, 8);
      String timeOfDay = TimeHelper.getTimeOfTheDay(time);
      expect(timeOfDay, 'Morning');
    });
    
    test('should return Afternoon', () {
      DateTime time = DateTime(2021, 1, 1, 13);
      String timeOfDay = TimeHelper.getTimeOfTheDay(time);
      expect(timeOfDay, 'Afternoon');
    });
    
    test('should return Evening', () {
      DateTime time = DateTime(2021, 1, 1, 20);
      String timeOfDay = TimeHelper.getTimeOfTheDay(time);
      expect(timeOfDay, 'Evening');
    });
    
  });



}
