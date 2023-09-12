#!/usr/bin/node
const dict = require('./101-data').dict;

const vals = [...new Set(Object.values(dict))]; // to get the uniqe values from dict
const keys = Object.keys(dict);

const newDict = {};
for (const v in vals) {
  const list = [];
  for (const k in keys) {
    if (dict[keys[k]] === vals[v]) {
      list.push(keys[k]);
    }
  }
  newDict[vals[v]] = list;
}
console.log(newDict);

// Another way to solv this problem by iterating  over Object.entries(dict) instead of Object.keys(dict)
/**
const vals = [...new Set(Object.values(dict))]; // to get uniqe values
const dickList = Object.entries(dict);

const newDict = {};
for (const v in vals) {
  const list = [];
  for (const i in dickList) {
    if (dickList[i][1] === vals[v]) {
      list.push(dickList[i][0]);
    }
  }
  newDict[vals[v]] = list;
}
console.log(newDict);

 */
