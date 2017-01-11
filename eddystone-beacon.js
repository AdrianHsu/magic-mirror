// by Adrian Hsu
var eddystoneBeacon = require('eddystone-beacon');
var url = 'https://goo.gl/T3QufX';

eddystoneBeacon.advertiseUrl(url, [options]);
console.log('Beacon is running!');
