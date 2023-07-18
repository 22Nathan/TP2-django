

<script>

    /** @type {any} */
    let promise = ""

    async function send(){
        const res = await fetch('http://127.0.0.1:8000/animals/')
        if (res.ok) {
            let gg = await res.json()
            console.log(gg[0])
            return gg
        } else {
            throw new Error('Request failed')
        }
    }

    function reset(){
        promise = ""
    }

</script>

<!-- -------------------------------------------- -->

    <div class="rounded-lg border border-white/10 p-10 bg-white/5 backdrop-blur-sm flex flex-col gap-10">
                    
        <div class="flex gap-2 justify-between">
            <p class="text-xl">
                GET 
                <span class="text-base text-white/50">10 premiers</span>
            </p>
            <div class="flex gap-3">
                <button class="rounded-md px-5 py-2 bg-black border border-white/20 hover:border-white/80 duration-150 flex items-center gap-2"
                on:click={()=>{ reset() }}
                >
                    Vider
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M9.75 9.75l4.5 4.5m0-4.5l-4.5 4.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>                                                 
                </button>
                <button class="rounded-md px-5 py-2 bg-black border border-white/20 hover:border-white/80 duration-150 flex items-center gap-2"
                    on:click={()=>{ promise = send() }}
                >
                    Envoyer
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M6 12L3.269 3.126A59.768 59.768 0 0121.485 12 59.77 59.77 0 013.27 20.876L5.999 12zm0 0h7.5" />
                    </svg>                              
                </button>
            </div>
        </div>
        
        <div class="h-px bg-white/10 w-[calc(100%+80px)] -translate-x-10"/>

        <div class="flex flex-col lg:flex-row gap-2">
            <button class="self-end h-fit rounded-md px-5 py-2 bg-black border border-white/20 hover:border-white/80 duration-150 flex items-center gap-2"
                on:click={()=>{ promise = send() }}
            >
                Actualiser
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99" />
                </svg>                                            
            </button>
        </div>

        <div class="flex flex-col gap-2">
            <p>Resultat</p>
            <div class="p-10 rounded-lg bg-white/5 text-sm">
                {#await promise}
                    <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                {:then res}
                    <div class="flex flex-col gap-4 divide-y divide-white/20">
                        {#each res as r }
                            <div class="flex flex-wrap gap-1 pt-4">
                                {#each Object.keys(r) as key }
                                    <p class="px-3 bg-white/5 rounded flex gap-3 flex-nowrap">
                                        <span class="text-white/80 uppercase"> {key} </span> 
                                        : 
                                        <span class="text-white"> {r[key]} </span>
                                    </p>
                                {/each}
                            </div>
                        {/each}
                    </div>
                {:catch error}
                    <p class="text-red-500">{error}</p>
                {/await}
            </div>
        </div>

    </div>