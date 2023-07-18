

<script>

    import Get from "$lib/components/Get.svelte"

</script>

<!-- -------------------------------------------- -->

    <main class="pb-20">
        <header class="container mx-auto pt-36 pb-32 md:pb-36 md:pt-56 text-center flex flex-col items-center">
            <h1 class="title text-5xl md:text-7xl lg:text-8xl max-w-[720px] mb-10">
                <span class="relative z-30">
                    TP2 SAFARIO
                </span>
            </h1>
            <p class="text-xl md:text-3xl mb-20 lg:mb-24 relative z-30 max-w-[520px]">
                <span class="gradient-heading-1">Nathan ROSSI</span>
                -
                <span class="gradient-heading-3">Shamnawaz SUBA KHAN</span>
            </p>
            <div class="animate-bounce bg-slate-800 p-2 w-10 h-10 ring-1 ring-white/20 shadow-lg rounded-full flex items-center justify-center">
                <svg class="w-6 h-6 text-white/80" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                  <path d="M19 14l-7 7m0 0l-7-7m7 7V3"></path>
                </svg>
            </div>
        </header>

        <div class="container mx-auto flex flex-col gap-10">

            <Get/>

        </div>
    </main>

<!-- -------------------------------------------- -->

<style>

</style>