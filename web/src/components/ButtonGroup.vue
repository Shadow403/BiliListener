<script setup>
  import { watchEffect } from 'vue';
  import { NButton, NButtonGroup } from 'naive-ui';

  const props = defineProps({
    buttons: {
      type: Array,
      required: true
    },
    defaultButtonId: {
      type: [String, Number],
      required: false
    }
  });

  const emit = defineEmits(['update:buttons', 'button-click']);

  const handleClick = (id) => {
    const newButtons = props.buttons.map((button) => ({
      ...button,
      isClick: button.id === id,
      type: button.id === id ? 'primary' : 'default'
    }));
    emit('update:buttons', newButtons);
    emit('button-click', id);
  };

  watchEffect(() => {
    if (props.defaultButtonId) {
      const defaultButton = props.buttons.find(button => button.id === props.defaultButtonId);
      if (defaultButton) {
        defaultButton.isClick = true;
      }
    }
  });
</script>

<template>
  <n-button-group>
    <n-button
      v-for="button in buttons"
      :key="button.id"
      :type="button.isClick ? 'primary' : 'default'"
      @click="handleClick(button.id)"
    >
      {{ button.label }}
    </n-button>
  </n-button-group>
</template>
