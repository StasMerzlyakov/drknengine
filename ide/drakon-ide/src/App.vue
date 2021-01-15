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
                    <b-nav-item-dropdown :text="$t('messages.schema')">
                        <b-dropdown-item-button @click="loadDialogue">
                            <input type="file" ref="loadFile" class="d-none" @change="onLoadFileChange"/>
                            <span>{{ $t("messages.load") }}</span>
                        </b-dropdown-item-button>
                        <b-dropdown-item-button @click="saveDialogue">
                            <input type="file" ref="saveFile" class="d-none" @change="onSaveFileChange"/>
                            <span>{{ $t("messages.save") }}</span>
                        </b-dropdown-item-button>
                    </b-nav-item-dropdown>
                    <b-nav-item-dropdown :text="$t('messages.locale')">
                        <b-dropdown-item href="#" v-for="(lang, index) in langs" :key="index"  v-on:click="setLocale(lang)" :value="lang">{{ lang }}</b-dropdown-item>
                    </b-nav-item-dropdown>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
        <!-- <img alt="DRAKON Engine" src="./assets/drakosha104.png"> -->
        <DrakonEditor ref="drakonEditor"/>
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
        return { 
            langs: this.$root.getLocales(),
        }
    },
    methods: {
        setLocale (locale) {
            this.$root.setLocale(locale)
        },
        loadDialogue() {
            this.$refs.loadFile.click()
        },
        onLoadFileChange(e) {
            var files = e.target.files || e.dataTransfer.files;
            if (!files.length)
                return;
            var reader = new FileReader()
            var file = files[0]
            reader.readAsText(file)
            
            var refs = this.$refs
            reader.onload = function() {
                refs.drakonEditor.importSvg(reader.result)
            }

            reader.onerror = function() {
                console.log(reader.error)
            }
        },
        onSaveFileChange(e) {
            var files = e.target.files || e.dataTransfer.files;
            if (!files.length)
                return;
            //var file = files[0]
            function onInitFs(fs) {
            
                fs.root.getFile('log.txt', {create: true, exclusive: true}, function() {
                  // fileEntry будет иметь следующие свойства
                  // fileEntry.isFile === true
                  // fileEntry.name == 'log.txt'
                  // fileEntry.fullPath == '/log.txt'
            
                });
            
            }
            window.requestFileSystem = window.requestFileSystem || window.webkitRequestFileSystem || window.mozRequestFileSystem;
            window.requestFileSystem(window.PERSISTENT, 1024*1024, onInitFs);        
        },
        saveDialogue() {
            this.$refs.saveFile.click()
        },
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
