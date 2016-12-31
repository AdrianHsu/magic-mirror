// by Adrian Hsu
var eddystoneBeacon = require('eddystone-beacon');

//var namespaceId = '00010203040506070809';
//var instanceId = 'aabbccddeeff';

var url = 'https://goo.gl/T3QufX';
var options = {
  txPowerLevel: -22,  // override TX Power Level, default value is -21, 
  tlmCount: 2,       // 2 TLM frames 
  tlmPeriod: 10      // every 10 advertisements 
};

//eddystoneBeacon.advertiseUid(namespaceId, instanceId, [options]);
eddystoneBeacon.advertiseUrl(url, [options]);

console.log('Beacon is running!');
