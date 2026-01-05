// import {forEach} from './forEach'

const { forEach } = require('../forEach')


const mockCallback = jest.fn(x => 17 + x)

const trueMockFn = jest.fn().mockReturnValue(true)

const limitedValMockFn = jest.fn().mockReturnValueOnce(17).mockReturnValueOnce(10)

describe("Mock Function Test calls", () => {

    test('forEach Callback mock function test', () => {

        forEach([0, 1], mockCallback)

        expect(mockCallback.mock.calls).toHaveLength(2)

        mockCallback.mock.calls.forEach(call => {
            expect(call.length).toBe(1)
        })


        expect(mockCallback.mock.calls[0][0]).toBe(0)

        expect(mockCallback.mock.calls[1][0]).toBe(1)

        expect(mockCallback.mock.results[0].value).toBe(17)

        expect(mockCallback.mock.results[1].value).toBe(18)

    })

    test("true Mock Func Test", () => {
        expect(trueMockFn()).toBeTruthy()
    })

    test("Limited Val Test", () => {
        expect(limitedValMockFn()).toBe(17)
        expect(limitedValMockFn()).toBe(10)
        expect(limitedValMockFn()).toBeUndefined()
    }

    )




})