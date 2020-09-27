import 'package:flutter/material.dart';
import 'pageselector.dart';
import 'pages.dart';
import 'package:google_fonts/google_fonts.dart';

class TabletMode extends StatefulWidget {
  @override
  _TabletModeState createState() => _TabletModeState();
}

class _TabletModeState extends State<TabletMode> {
  @override
  Widget build(BuildContext context) {
    return Container(
      color: Color.fromRGBO(249, 247, 255, 1),
      child: Row(
        children: <Widget>[
          Flexible(
            flex: 1,
            child: Container(
              decoration: BoxDecoration(
                  borderRadius: BorderRadius.all(Radius.circular(14)),
                  color: Colors.white),
              clipBehavior: Clip.antiAlias,
              constraints: BoxConstraints(maxWidth: 300),
              padding: EdgeInsets.all(5),
              margin: EdgeInsets.all(10),
              child: Column(
                children: [
                  Material(
                      color: Colors.transparent,
                      child: Container(
                          padding: EdgeInsets.all(10),
                          child: ListTile(
                            leading: new Image.asset(
                                'assets/images/TURateLogoDraft1.png'),
                            title: Text(
                              'Lecturate',
                              style: GoogleFonts.getFont(
                                'Nunito',
                                fontSize: 35,
                                fontWeight: FontWeight.w700,
                              ),
                            ),
                          ))),
                  PageSelection(
                    pages,
                  )
                ],
              ),
            ),
          ),
          Flexible(
              flex: 3,
              child: Center(
                child: Text(
                  'Selected Page',
                  style: TextStyle(color: Colors.black),
                ),
              ))
        ],
      ),
    );
  }
}
