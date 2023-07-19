

<script>

    import { onMount } from "svelte"

    onMount(()=>{
        send()
    })

    /** @type {any} */
    let promise = ""

    async function send(){
        const res = await fetch('http://127.0.0.1:8000/nbAnimals')
        if (res.ok) {
            promise = await res.json() 
        } else {
            throw new Error('Request failed')
        }
    }

</script>

<!-- -------------------------------------------- -->

    <div class="rounded-lg border border-white/10 p-10 bg-white/5 backdrop-blur-sm flex flex-col gap-10">
                    
        <div class="flex gap-2 justify-between">
            <p class="text-xl">
                Nombre d'animaux 
                <span class="text-base text-white/50"></span>
            </p>
        </div>
        
        <div class="h-px bg-white/10 w-[calc(100%+80px)] -translate-x-10"/>

        <div class="flex flex-col lg:flex-row gap-2">
            <button class="self-end h-fit rounded-md px-5 py-2 bg-black border border-white/20 hover:border-white/80 duration-150 flex items-center gap-2"
                on:click={()=>{ send() }}
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
                        {res}
                    </div>
                {:catch error}
                    <p class="text-red-500">{error}</p>
                {/await}
            </div>
        </div>

    </div>