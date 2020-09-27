import 'Selector.dart';
import 'package:flutter/material.dart';

SelectorItem lectures = SelectorItem(
    text: 'Lectures',
    icon: Icon(
      Icons.description,
      color: Colors.blue,
    ));
SelectorItem categories = SelectorItem(
    text: 'Categories',
    icon: Icon(
      Icons.explore,
      color: Colors.indigo,
    ));
SelectorItem professors = SelectorItem(
    text: 'Professors',
    icon: Icon(
      Icons.contacts,
      color: Colors.purple,
    ));
SelectorItem search = SelectorItem(
    text: 'Search',
    icon: Icon(
      Icons.search,
      color: Colors.deepPurple,
    ));
SelectorItem bookmark = SelectorItem(
    text: 'Bookmark',
    icon: Icon(
      Icons.favorite_border,
      color: Colors.pink,
    ));
SelectorItem settings = SelectorItem(
    text: 'Settings',
    icon: Icon(
      Icons.settings,
      color: Colors.grey[700],
    ));
SelectorItem operation = SelectorItem(text: 'Operation');
List<SelectorItem> pages = [
  lectures,
  categories,
  professors,
  search,
  bookmark,
  settings,
];
