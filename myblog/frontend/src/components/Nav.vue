<template>
  <nav id="sidebar">

  </nav>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import { UPDATE_CATEGORIES, UPDATE_POSTS } from '@/store/mutation-types'

export default {
  name: 'site-sidebar',
  data () {
    // URL内のGETパラメータを参照
    return {
      keyword: this.$router.query.keyword || '',
      selected: this.$router.query.category || ''
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
#sidebar {
  width: 160px;
}
</style>
