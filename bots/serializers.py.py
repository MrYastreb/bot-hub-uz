from rest_framework import serializers
from .models import Bot, Scenario, Block, Button

class ButtonSerializer(serializers.ModelSerializer):
    target_block_id = serializers.PrimaryKeyRelatedField(
        queryset=Block.objects.all(),
        source='target_block',
        allow_null=True,
        required=False
    )

    class Meta:
        model = Button
        fields = ['id', 'text', 'action_type', 'url', 'target_block_id']


class BlockSerializer(serializers.ModelSerializer):
    buttons = ButtonSerializer(many=True)

    class Meta:
        model = Block
        fields = ['id', 'title', 'message_text', 'order', 'buttons']

    def create(self, validated_data):
        buttons_data = validated_data.pop('buttons')
        block = Block.objects.create(**validated_data)
        for button_data in buttons_data:
            Button.objects.create(block=block, **button_data)
        return block


class ScenarioSerializer(serializers.ModelSerializer):
    blocks = BlockSerializer(many=True)

    class Meta:
        model = Scenario
        fields = ['id', 'name', 'description', 'is_active', 'blocks']


class BotSerializer(serializers.ModelSerializer):
    scenarios = ScenarioSerializer(many=True, read_only=True)

    class Meta:
        model = Bot
        fields = ['id', 'name', 'token', 'username', 'webhook_url', 'scenarios']