
// test/app.test.js

const request = require('supertest');
const chai = require('chai');
const app = require('../app'); // path to your app.js file

const expect = chai.expect;

describe('Coffee Delivery Service API', () => {
    describe('GET /coffees', () => {
        it('should return a list of available coffees', (done) => {
            request(app)
                .get('/coffees')
                .end((err, res) => {
                    expect(res.statusCode).to.equal(200);
                    expect(res.body).to.be.an('array');
                    done();
                });
        });
    });

    describe('GET /orders', () => {
        it('should return a list of placed orders', (done) => {
            request(app)
                .get('/orders')
                .end((err, res) => {
                    expect(res.statusCode).to.equal(200);
                    expect(res.body).to.be.an('array');
                    done();
                });
        });
    });
});
