
const sum = (a, b) => {

    return a + b
}

const compileErrorCode = () => {
    throw new Error('ERROR 404: you are running into an error!! ')
}

describe("Testing different matchers", () => {

    test("adds 1 + 2 and expect 3", () => {
        expect(sum(1, 2)).toBe(3)
    })

    test("Object matcher", () => {
        const data = { one: 1, undefined }
        data['two'] = 2

        expect(data).toEqual({ one: 1, two: 2 })
    })

    // toStrictEqual does not ignore undefined values unlike toEqual
    test("Object matcher", () => {
        const data = { one: 1, undefined }
        data['two'] = 2

        expect(data).toStrictEqual({ one: 1, undefined, two: 2 })
    })

    test("matching null", () => {
        const n = null

        expect(n).toBeNull()
        expect(n).toBeDefined()
        expect(n).not.toBeUndefined()
        expect(n).not.toBeTruthy()
        expect(n).toBeFalsy()
    }),

        test("Matching zero", () => {

            const n = 0

            expect(n).not.toBeNull()
            expect(n).toBeDefined()
            expect(n).not.toBeUndefined()
            expect(n).not.toBeTruthy()
            expect(n).toBeFalsy()
        })

    test("Number Matchers", () => {
        const value = 2 + 2

        expect(value).toBe(4)
        expect(value).toBeGreaterThan(2)
        expect(value).toBeGreaterThanOrEqual(4)
        expect(value).toBeLessThan(5)
        expect(value).toBeLessThanOrEqual(4.5)
    })

    test("Floating number matcher", () => {
        const value = 0.1 + 0.3

        expect(value).toBeCloseTo(0.4)
    })

    test("Array Matchers", () => {

        const arr = [1, 2, 3]
        const string = "Hey There Jest"

        expect(arr).toContain(2)
        expect(arr).not.toContain(4)
        expect(string).toContain("Jest")
    })

    test("String Matchers", () => {

        expect("Arsenal").not.toMatch(/i/)

        expect("Arsenal").toMatch(/sen/)

    })

    test("Error matchers", () => {

        expect(() => compileErrorCode()).toThrow()
        expect(() => compileErrorCode()).toThrow(Error)

        expect(() => compileErrorCode()).toThrow(/404/)
    })


})

