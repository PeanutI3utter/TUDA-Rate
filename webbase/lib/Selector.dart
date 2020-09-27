import 'package:flutter/material.dart';

/// An Item that can be listed in a Selector
/// It consists of a text and an icon
class SelectorItem {
  String text;
  Icon icon;

  SelectorItem({
    @required this.text,
    this.icon,
  });
}

/// Custom ListView where the selected item is highlighted with a different
/// background color.
class Selector extends StatefulWidget {
  final List<SelectorItem> selectables;
  final SelectorItem selected;
  final ValueChanged<SelectorItem> itemSelectCallback;
  final Color color;
  final Color selectedColor;

  Selector(
      {@required this.selectables,
      @required this.itemSelectCallback,
      this.color,
      this.selectedColor,
      this.selected});

  @override
  _SelectorState createState() => _SelectorState();
}

class _SelectorState extends State<Selector> {
  List<SelectorItem> selectables;
  SelectorItem selected;
  ValueChanged<SelectorItem> itemSelectCallback;
  Color color;
  Color selectedColor;

  @override
  void initState() {
    super.initState();
    selectables = widget.selectables;
    itemSelectCallback = widget.itemSelectCallback;
    color = widget.color == null ? Colors.transparent : widget.color;
    selectedColor =
        widget.selectedColor != null ? widget.selectedColor : Colors.blue[100];
    selected = widget.selected != null ? widget.selected : selectables[0];
    itemSelectCallback(selected);
  }

  @override
  Widget build(BuildContext context) {
    return ListView(
      shrinkWrap: true,
      children: selectables.map((item) {
        ListTile content = ListTile(
          title: Text(
            item.text,
            style: TextStyle(
                color: item == selected ? Colors.white : Colors.black,
                fontSize: 20),
          ),
          leading: item.icon,
          onTap: () {
            itemSelectCallback(item);
            setState(() {
              selected = item;
            });
          },
        );
        return Card(
          child: content,
          shadowColor: Colors.transparent,
          color: item == selected ? selectedColor : Colors.transparent,
          margin: EdgeInsets.all(0),
        );
      }).toList(),
    );
  }

  SelectorItem selectedItem() {
    return selected;
  }
}
