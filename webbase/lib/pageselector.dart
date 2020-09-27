import 'package:flutter/material.dart';
import 'Selector.dart';

class PageSelection extends StatelessWidget {
  placeHolderFunc(item) => null;
  List<SelectorItem> pages;
  ValueChanged<SelectorItem> itemSelectCallback;

  PageSelection(List<SelectorItem> pages,
      {ValueChanged<SelectorItem> itemSelectCallback}) {
    this.pages = pages;
    this.itemSelectCallback =
        itemSelectCallback == null ? (item) => null : itemSelectCallback;
  }

  @override
  Widget build(BuildContext context) {
    return Container(
        padding: EdgeInsets.all(10),
        child: Selector(
            selectables: this.pages, itemSelectCallback: itemSelectCallback));
  }
}
