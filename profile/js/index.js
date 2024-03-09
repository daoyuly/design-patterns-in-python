(function demo(){
    function profile() {
        window.performance.mark('mark_1')
        console.log(`window.performance.mark('mark_1')`, performance.getEntriesByName('mark_1'))

        window.performance.mark('mark_2')
        console.log(`window.performance.mark('mark_1')`, performance.getEntriesByName('mark_2'))

        window.performance.mark('mark_1')
        console.log(`window.performance.mark('mark_1')`, performance.getEntriesByName('mark_1'))

        performance.getEntriesByName('mark_1')


    }

    profile()
})()