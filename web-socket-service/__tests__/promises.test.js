
const fetchDataPromise = () => {

    return new Promise((resolve, reject) => {

        const success = true

        setTimeout(() => {
            if (success) {
                resolve("Data Fetched Success")
            } else {
                reject("Data Fetch Failed")
            }
        }, 2000)

    })
}

const fetchDataAsyncAwait = () => {

    return new Promise((resolve, reject) => {

        const success = false

        setTimeout(() => {
            if (success) {
                resolve("Data Fetched Success")
            } else {
                reject("Data Fetch Failed")

            }
        }, 3000)

    })
}

describe("Async Test Group", () => {


    test("Promise Testing", () => {
        return fetchDataPromise().then((data) => {
            expect(data).toContain("Success")
        })
    })

    test("Async/await testing", async () => {

        const result = await fetchDataPromise()

        expect(result).toContain("Success")

    })

    // Handling failure situations for promises

    test("Promise Failure Scenario", async () => {
        expect.assertions(1)

        try {
            await fetchDataAsyncAwait()
        } catch (error) {

            expect(error).toMatch('Failed')

        }
    })

    test('Test Success' , async() => {

        await expect(fetchDataPromise()).resolves.toBe("Data Fetched Success")

    } )

    test("Test Failed" , async() => {
        await expect(fetchDataAsyncAwait()).rejects.toContain("Failed")
    })


})




