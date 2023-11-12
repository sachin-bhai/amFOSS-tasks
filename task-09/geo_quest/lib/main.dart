import 'package:flutter/material.dart';
import 'package:flutter_osm_plugin/flutter_osm_plugin.dart';
import 'package:geo_quest/welcome.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      
      theme: ThemeData(
        // This is the theme of your application.
        //
        // TRY THIS: Try running your application with "flutter run". You'll see
        // the application has a blue toolbar. Then, without quitting the app,
        // try changing the seedColor in the colorScheme below to Colors.green
        // and then invoke "hot reload" (save your changes or press the "hot
        // reload" button in a Flutter-supported IDE, or press "r" if you used
        // the command line to start the app).
        //
        // Notice that the counter didn't reset back to zero; the application
        // state is not lost during the reload. To reset the state, use hot
        // restart instead.
        //
        // This works for code too, not just values: Most code changes can be
        // tested with just a hot reload.
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: WelcomePage(),
    );
  }
}
class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}


class _MyHomePageState extends State<MyHomePage> {
  List<GeoPoint> markedList = [];
  bool marked = false;
  late RoadInfo roadInfo;
  final mapController = MapController.withUserPosition(
    trackUserLocation: const UserTrackingOption(
      enableTracking: true,
      unFollowUser: false,
    ),
  );

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((timeStamp) {
      mapController.listenerMapLongTapping.addListener(() async {
        if (markedList.isNotEmpty) {
          await mapController.removeMarker(markedList[0]);
          await mapController.clearAllRoads();
          markedList.removeAt(0);
          marked = false;
          
        }

        GeoPoint userLocation = await mapController.myLocation();
        var position = mapController.listenerMapLongTapping.value;

        if (position != null) {
          markedList.add(position);
          await mapController.addMarker(position,
              markerIcon: const MarkerIcon(
                icon: Icon(
                  Icons.location_on,
                  color: Colors.amber,
                  size: 45,
                ),
              ));

          roadInfo = await mapController.drawRoad(
            userLocation,
            GeoPoint(
                latitude: position.latitude, longitude: position.longitude),
            roadType: RoadType.car,
            roadOption: RoadOption(
              roadWidth: 10,
              roadColor: Colors.red.shade900,
              zoomInto: true,
            ),
          );
          marked = true;
          
        }

        setState(() {});
      });
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
      body: OSMFlutter(
        controller: mapController,
        osmOption: OSMOption(
          userTrackingOption: const UserTrackingOption(
            enableTracking: true,
            unFollowUser: false,
          ),
          zoomOption: const ZoomOption(
            initZoom: 8,
            minZoomLevel: 3,
            maxZoomLevel: 19,
            stepZoom: 1.0,
          ),
          userLocationMarker: UserLocationMaker(
            personMarker: const MarkerIcon(
              icon: Icon(
                Icons.person_pin_circle_outlined,
                color: Colors.black,
                size: 100,
              ),
            ),
            directionArrowMarker: const MarkerIcon(
              icon: Icon(
                Icons.double_arrow,
                size: 35,
              ),
            ),
          ),
          roadConfiguration: const RoadOption(
            roadColor: Colors.blue,
          ),
          markerOption: MarkerOption(
            defaultMarker: const MarkerIcon(
              icon: Icon(
                Icons.person_pin_circle,
                color: Colors.blue,
                size: 56,
              ),
            ),
          ),
        ),
        onMapIsReady: (isReady) async {
          if (isReady) {
            await Future.delayed(const Duration(seconds: 1), () async {
              await mapController.currentLocation();
            });
          }
        },
      ),
      bottomNavigationBar: marked
          ? BottomAppBar(
              color: Colors.blueGrey.shade900,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: [
                  Text(
                    '  Time\n ${roadInfo.duration! ~/ 60} min',
                    style: const TextStyle(
                        color: Colors.amber,
                        fontSize: 20,
                        fontFamily: 'BleedingCowboys'),
                  ),
                  Text(
                    'Distance\n  ${roadInfo.distance!.toInt()} km',
                    style: const TextStyle(
                        color: Colors.amber,
                        fontSize: 20,
                        fontFamily: 'BleedingCowboys'),
                  ),
                ],
              ),
            )
          : BottomAppBar(
              color: Colors.blueGrey.shade900,
              child: const Padding(
                padding: EdgeInsets.all(5.0),
                child: Center(
                  child: Text(
                    'Long press to add next location',
                    style: TextStyle(
                        color: Colors.white,
                        fontSize: 20,
                        fontFamily: 'BleedingCowboys'),
                  ),
                ),
              ),
            ),
    );
  }
}