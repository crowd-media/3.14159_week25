<script>
    import { goto } from '$app/navigation';
</script>

<main>
    <h1>El Debate</h1>
    
    <div class="header"> 
        <div class=botton_prompt>
            <button on:click={()=>goto("configure")}> 
                CONFIGURE
            </button>
        </div>
        <div class=botton_conversation>
            <button on:click={()=>goto("play")}> 
                PLAY CONVERSATION
            </button>
        </div>
    </div>
    <slot />
</main>

<style>
    main {
      font-family: sans-serif;
      text-align: center;
      margin: 40px auto;
    }
    .header {
      text-align: center;
              box-shadow: 6px 6px 10px rgba(34, 34, 34, 0.2), -6px -6px 10px #fff;
      padding: 10px;
              box-sizing: border-box;
      border-radius: 20px;
      display: flex;
      flex-direction: row;
      justify-content: space-evenly;
      margin:20px;
  }
  button{
    font-size: 20px;
  }
</style>
