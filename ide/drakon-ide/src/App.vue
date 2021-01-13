<template>
    <div id="app">
            <b-navbar toggleable="lg" type="dark" variant="info">
                <b-navbar-brand href="#">{{ $t("messages.editor_name") }}</b-navbar-brand>
            
                <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            
                <b-collapse id="nav-collapse" is-nav>
                  <!-- <b-navbar-nav>
                    <b-nav-item href="#">Link</b-nav-item>
                    <b-nav-item href="#" disabled>Disabled</b-nav-item>
                  </b-navbar-nav> -->
            
                  <b-navbar-nav class="ml-auto">
                    <!-- <b-nav-form>
                      <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
                      <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
                    </b-nav-form> -->
            
                     <b-nav-item-dropdown :text="$t('messages.locale')" right>
                  <!--    <b-dropdown-item href="#" v-for="(lang, index) in langs" :key="index"  v-on:click="$i18n.setLocaleMessage(lang)" :value="lang">{{ lang }}</b-dropdown-item> -->
                       <b-dropdown-item href="#" v-for="(lang, index) in langs" :key="index"  v-on:click="setLocale(lang)" :value="lang">{{ lang }}</b-dropdown-item>
                     </b-nav-item-dropdown>
                   </b-navbar-nav>
                </b-collapse>
              </b-navbar>
        <!-- <img alt="DRAKON Engine" src="./assets/drakosha104.png"> -->
        <DrakonEditor/>
    </div>
</template>

<script>
import DrakonEditor from './components/DrakonEditor.vue'

export default {
  name: 'App',
  components: {
       DrakonEditor
    },
   data () {
     return { langs: ['ru', 'en'] }
  },
  methods: {
    setLocale (locale) {
       console.log(locale);
    }
  }
}
  
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
