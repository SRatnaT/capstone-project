
function asyncFetchData(callback) {

    setTimeout(() => {
        const success = true

        if (success) {

            callback("Data Fetched Successfully")

        } else {

            callback("Error in Data Fetching")
        }
    }, 2000)

}

asyncFetchData((data) => {

    console.log(data);

})


function calculate(a , b , operationCallback){

    setTimeout(() => {
        const mode = "subs"
        
        operationCallback( a, b , mode)

    } , 1000)
}


calculate(1 , 2 , (a , b , mode) => {
    
    if (mode === "addition"){
        console.log(a + b);
        
    }else{
        console.log(a - b);
        
    }
})