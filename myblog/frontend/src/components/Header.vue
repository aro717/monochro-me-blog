<template>
  <header>
    <h1>
      <router-link :to="{name: 'posts'}">Monochro-me</router-link>
    </h1>
    <div id="form">
      <input type="text" placeholder="Search" class="text" v-model="keyword" @change="search">
      <div class="selectWrap">
        <select class="select" v-model="selected" @change="search">
          <option value="" :key="-1">Category</option>
          <option v-for="category of categoryList" :value="category.id" :key="category.id">{{category.name}}</option>
        </select>
      </div>
    </div>
  </header>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import { UPDATE_CATEGORIES, UPDATE_POSTS } from '@/store/mutation-types'

export default {
  name: 'site-header',
  data () {
    // URL内のGETパラメータを参照
    return {
      keyword: this.$router.query.keyword || '',
      selected: this.$router.query.category || ''
    }
  },
  watch: {
    // サイトタイトルクリックでトップページに戻る
    '$route' () {
      this.keyword = this.$router.query.keyword || ''
      this.selected = this.$router.query.category || ''
    }
  },
  created () {
    this.$http(this.$httpCategories)
      .then(response => {
        return response.json()
      })
      .then(data => {
        this[UPDATE_CATEGORIES](data)
      })
  },
  computed: {
    ...mapGetters(['categoryList'])
  },
  methods: {
    ...mapActions([UPDATE_CATEGORIES, UPDATE_POSTS]),
    search () {
      this.$router.push({ name: 'posts', query: { page: 1, keyword: this.keyword, category: this.selected } })
    }
  }
}
</script>

<style scoped>
header {
  background-color: #f8f8f2;
  color: #272822;
  height: 50px;
  display: grid;
  grid-template-columns: 20px 1fr 20px;
  grid-template-rows: 1fr;
  margin-bottom: 80px;
}

header > * {
  grid-row: 1;
  grid-column: 2;
}

h1 {
  justify-self: start;
  align-self: center;
  font-size: 20px;
  font-weight: normal;
}

h1 > a {
  color: #272822;
  text-decoration: none;
}

#form {
  justify-self: end;
  align-self: center;
  display: none;
}

.text {
  border-bottom: solid 1px #444;
  border-right: none;
  border-top: none;
  border-left: none;
  background-color: transparent;
  color: #272822;
  width: 200px;
  margin-left: 20px;
  padding-left: 6px;
  padding-bottom: 1px;
  font-family: fot-tsukuardgothic-std, sans-serif;
}

.selectWrap {
  margin-left: 20px;
  width: 150px;
  position: relative;
  display: inline-block;
}

.selectWrap::after {
  content: '';
  width: 6px;
  height: 6px;
  border: 0;
  border-bottom: solid 2px #444;
  border-right: solid 2px #444;
  -ms-transform: rotate(45deg);
  -webkit-transform: rotate(45deg);
  transform: rotate(45deg);
  position: absolute;
  top: 50%;
  right: 10px;
  margin-top: -4px;
}

.select {
  appearance: none;
  border-bottom: solid 1px #444;
  border-right: none;
  border-top: none;
  border-left: none;
  background-color: transparent;
  color: #000;
  width: 100%;
  font-family: fot-tsukuardgothic-std, sans-serif;
}

::placeholder {
  color: #000;
  opacity: 1;
  font-family: fot-tsukuardgothic-std, sans-serif;
}

@media (min-width: 768px) {
  header {
    grid-template-columns: 1fr 700px 1fr;
  }

  #form {
    display: block;
  }
}

@media (min-width: 1024px) {
  header {
    grid-template-columns: 1fr 980px 1fr;
  }
}
</style>
