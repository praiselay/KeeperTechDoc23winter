const express = require('express');
const {spawn} = require('child_process'); // const spawn = require('child_process').spawn;과 같음
const app = express();
const port = 5500;

app.use(express.json());

